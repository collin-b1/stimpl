from stimpl.expression import *
from stimpl.runtime import *

if __name__=='__main__':
  program = Print(Program(
            Assign(Variable("i"), IntLiteral(0)),
            Assign(Variable("j"), Assign(Variable("i"),
                   Add(Variable("i"), IntLiteral(1)))),
            Assign(Variable("k"), Assign(Variable("i"),
                   Add(Variable("i"), IntLiteral(1)))),
            Assign(Variable("l"), Assign(Variable("i"),
                   Add(Variable("i"), IntLiteral(1)))),
        ))
  run_stimpl(program)
