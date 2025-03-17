# Token type
# EOF (End Of File) -> token is used to indicate that there is no more input left for lexical analysis
INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"


class Token(object):
    def __init__(self, type, value):
        # token types: INTEGER, PLUS OR EOF
        self.type = type
        # token value: 0.1,2,...,9 , "+" or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(type=self.type, value=self.value)

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, eg "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """
        Lexical analyzer (also known as scanner or tokenizer)
        This method is resposible for breaking a sentence apart into tokens. One token at a time
        """
        text = self.text

        """
        Is self.pos is past the end of the self.text?
        If so, then return EOF token because there is no more input left to convert into token
        """
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        """
        get a character at the position self.pos and decide, what token to create based on the single character
        """
        current_char = text[self.pos]

        """
        If the character is a digit then convert it to interger -> increment self.pos -> increment self.pos index
        to point to the next character after the digit -> return the INTEGER token
        """

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        """
        Compare the current token type with the passed token type and if they match 
        then "eat" the curren token and assign the next token to the self.currnet_token,
        otherwise raise an exception 
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """
        expr: INTEGER PLUS INTEGER 
        set current token to the first token taken from the input 
        """
        self.current_token = self.get_next_token()
        print(self.current_token)
        # we expect the curren token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(PLUS)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)

        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input

        result = left.value + right.value
        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()
