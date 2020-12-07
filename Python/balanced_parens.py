def balanced_parens(n):

    for each balanced expression of n-1 parentheses 
        for each pos i from 0 to m of an expression
            add '('
       for each pos  j from i + 1 to m
          add ')' if expression is balanced


balanced_parens(1)