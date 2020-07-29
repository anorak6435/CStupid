from .Data.Token import Token
from ..Errors.Error_Tokenizer import UnmatchedSourceError
import re

class Tokenizer:
    def __init__(self, queries):
        # the tokenQueries are the parts of the tokenizer
        # that search for the tokens in the source code
        self.tokenQueries = queries
        # the location of the tokens
        self.line = 1
        self.index = 0

    def search_tokens_in_source(self, sourceCode):
        savedTokens = []
        queryIndex = 0
        while queryIndex < len(self.tokenQueries):
            query = self.tokenQueries[queryIndex]
            # if the source code matches this query
            QueryMatch = re.match(query.getValue(), sourceCode)
            if QueryMatch:
                queryIndex = 0
                if query.name == "NewLine":
                    self.line += 1
                    self.index = 0
                else:
                    if query.name != "Whitespace":
                        savedTokens.append(Token(query.name, QueryMatch.group(query.matchGroup), self.line, self.index))
                    self.index += len(QueryMatch.group(0))
                sourceCode = sourceCode[len(QueryMatch.group(0)):]
                continue # go do the next iteration of the loop
            
            queryIndex += 1
        return savedTokens


    def getTokenList(self, sourceCode):
        token_list = []
        while (len(sourceCode) > 0):
            token = self.getNextToken(sourceCode)
            sourceCode = self.shortenSourceCode(sourceCode, token)
            token_list.append(token)
        return token_list


    def shortenSourceCode(self, sourceCode, token):
        return sourceCode[len(token.fullMatch):]

    def getNextToken(self, sourceCode):
        token = self.getNextTokenMatch(sourceCode)
        if token:
            self.updateLocationTracker(token)
            return token
        
        if len(sourceCode) > 0:
            raise UnmatchedSourceError(sourceCode, self.line, self.index)

    def getNextTokenMatch(self, sourceCode):
        queryIndex = 0
        nextToken = None
        while queryIndex < len(self.tokenQueries):
            query = self.tokenQueries[queryIndex]
            matchQuery = re.match(query.getValue(), sourceCode)
            if matchQuery:
                nextToken = Token(query.getTokenType(), matchQuery.group(query.matchGroup), self.line, self.index, matchQuery.group(0))
                queryIndex = len(self.tokenQueries)
                continue
            queryIndex += 1
        return nextToken

    def updateLocationTracker(self, token):
        if token.name == "NewLine":
            self.line += 1
            self.index = 0
        else:
            self.index += len(token.fullMatch)
