# Generated from PythonToJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,2,1,2,1,2,5,2,
        41,8,2,10,2,12,2,44,9,2,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,78,8,7,10,7,12,7,81,9,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,89,8,7,1,7,1,7,1,7,5,7,94,8,7,10,7,12,
        7,97,9,7,1,7,0,1,14,8,0,2,4,6,8,10,12,14,0,1,1,0,9,12,103,0,20,1,
        0,0,0,2,23,1,0,0,0,4,37,1,0,0,0,6,48,1,0,0,0,8,50,1,0,0,0,10,54,
        1,0,0,0,12,57,1,0,0,0,14,88,1,0,0,0,16,19,3,2,1,0,17,19,3,6,3,0,
        18,16,1,0,0,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,
        0,0,0,21,1,1,0,0,0,22,20,1,0,0,0,23,24,5,1,0,0,24,25,5,13,0,0,25,
        27,5,2,0,0,26,28,3,4,2,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,
        0,29,30,5,3,0,0,30,34,5,4,0,0,31,33,3,6,3,0,32,31,1,0,0,0,33,36,
        1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,34,1,0,0,0,37,
        42,5,13,0,0,38,39,5,5,0,0,39,41,5,13,0,0,40,38,1,0,0,0,41,44,1,0,
        0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,42,1,0,0,0,45,49,
        3,8,4,0,46,49,3,10,5,0,47,49,3,12,6,0,48,45,1,0,0,0,48,46,1,0,0,
        0,48,47,1,0,0,0,49,7,1,0,0,0,50,51,5,13,0,0,51,52,5,6,0,0,52,53,
        3,14,7,0,53,9,1,0,0,0,54,55,5,7,0,0,55,56,3,14,7,0,56,11,1,0,0,0,
        57,58,5,8,0,0,58,59,5,2,0,0,59,64,3,14,7,0,60,61,5,5,0,0,61,63,3,
        14,7,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        67,1,0,0,0,66,64,1,0,0,0,67,68,5,3,0,0,68,13,1,0,0,0,69,70,6,7,-1,
        0,70,89,5,14,0,0,71,89,5,13,0,0,72,73,5,13,0,0,73,74,5,2,0,0,74,
        79,3,14,7,0,75,76,5,5,0,0,76,78,3,14,7,0,77,75,1,0,0,0,78,81,1,0,
        0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,
        5,3,0,0,83,89,1,0,0,0,84,85,5,2,0,0,85,86,3,14,7,0,86,87,5,3,0,0,
        87,89,1,0,0,0,88,69,1,0,0,0,88,71,1,0,0,0,88,72,1,0,0,0,88,84,1,
        0,0,0,89,95,1,0,0,0,90,91,10,5,0,0,91,92,7,0,0,0,92,94,3,14,7,6,
        93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,15,1,
        0,0,0,97,95,1,0,0,0,10,18,20,27,34,42,48,64,79,88,95
    ]

class PythonToJavaParser ( Parser ):

    grammarFileName = "PythonToJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "':'", "','", "'='", 
                     "'return'", "'print'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NAME", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_func_def = 1
    RULE_params = 2
    RULE_stmt = 3
    RULE_var_assign = 4
    RULE_return_stmt = 5
    RULE_print_stmt = 6
    RULE_expr = 7

    ruleNames =  [ "program", "func_def", "params", "stmt", "var_assign", 
                   "return_stmt", "print_stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NAME=13
    NUMBER=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.Func_defContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.Func_defContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonToJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8578) != 0):
                self.state = 18
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 16
                    self.func_def()
                    pass
                elif token in [7, 8, 13]:
                    self.state = 17
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PythonToJavaParser.NAME, 0)

        def params(self):
            return self.getTypedRuleContext(PythonToJavaParser.ParamsContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)




    def func_def(self):

        localctx = PythonToJavaParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(PythonToJavaParser.T__0)
            self.state = 24
            self.match(PythonToJavaParser.NAME)
            self.state = 25
            self.match(PythonToJavaParser.T__1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 26
                self.params()


            self.state = 29
            self.match(PythonToJavaParser.T__2)
            self.state = 30
            self.match(PythonToJavaParser.T__3)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 31
                    self.stmt() 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(PythonToJavaParser.NAME)
            else:
                return self.getToken(PythonToJavaParser.NAME, i)

        def getRuleIndex(self):
            return PythonToJavaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = PythonToJavaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PythonToJavaParser.NAME)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 38
                self.match(PythonToJavaParser.T__4)
                self.state = 39
                self.match(PythonToJavaParser.NAME)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assign(self):
            return self.getTypedRuleContext(PythonToJavaParser.Var_assignContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(PythonToJavaParser.Return_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(PythonToJavaParser.Print_stmtContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = PythonToJavaParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.var_assign()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.return_stmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.print_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PythonToJavaParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonToJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)




    def var_assign(self):

        localctx = PythonToJavaParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PythonToJavaParser.NAME)
            self.state = 51
            self.match(PythonToJavaParser.T__5)
            self.state = 52
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonToJavaParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = PythonToJavaParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PythonToJavaParser.T__6)
            self.state = 55
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = PythonToJavaParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonToJavaParser.T__7)
            self.state = 58
            self.match(PythonToJavaParser.T__1)
            self.state = 59
            self.expr(0)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 60
                self.match(PythonToJavaParser.T__4)
                self.state = 61
                self.expr(0)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(PythonToJavaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PythonToJavaParser.NUMBER, 0)

        def NAME(self):
            return self.getToken(PythonToJavaParser.NAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToJavaParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonToJavaParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonToJavaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToJavaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(PythonToJavaParser.NUMBER)
                pass

            elif la_ == 2:
                self.state = 71
                self.match(PythonToJavaParser.NAME)
                pass

            elif la_ == 3:
                self.state = 72
                self.match(PythonToJavaParser.NAME)
                self.state = 73
                self.match(PythonToJavaParser.T__1)
                self.state = 74
                self.expr(0)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 75
                    self.match(PythonToJavaParser.T__4)
                    self.state = 76
                    self.expr(0)
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(PythonToJavaParser.T__2)
                pass

            elif la_ == 4:
                self.state = 84
                self.match(PythonToJavaParser.T__1)
                self.state = 85
                self.expr(0)
                self.state = 86
                self.match(PythonToJavaParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonToJavaParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 90
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 91
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 92
                    self.expr(6) 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




