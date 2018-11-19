# -*- generated by 1.0.12 -*-
import da
PatternExpr_322 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern325_'), da.pat.FreePattern(None)])
PatternExpr_329 = da.pat.FreePattern('a')
PatternExpr_357 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern360_'), da.pat.TuplePattern([da.pat.FreePattern('n2'), da.pat.FreePattern('v')])])
PatternExpr_388 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern391_'), da.pat.TuplePattern([da.pat.FreePattern('n2'), da.pat.FreePattern(None)])])
PatternExpr_424 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern427_'), da.pat.FreePattern(None)])
PatternExpr_431 = da.pat.FreePattern('a')
PatternExpr_471 = da.pat.TuplePattern([da.pat.ConstantPattern('preempt'), da.pat.FreePattern('n2')])
PatternExpr_510 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_515 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_558 = da.pat.TuplePattern([da.pat.ConstantPattern('prepare'), da.pat.FreePattern('n')])
PatternExpr_565 = da.pat.FreePattern('p')
PatternExpr_573 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.FreePattern('n2'), da.pat.FreePattern(None)])
PatternExpr_603 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.FreePattern('n2'), da.pat.FreePattern(None)])
PatternExpr_631 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_657 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern(None)])
PatternExpr_698 = da.pat.TuplePattern([da.pat.ConstantPattern('accept'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_711 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.FreePattern('n2'), da.pat.FreePattern(None)])
PatternExpr_748 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_753 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_797 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_823 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.BoundPattern('_BoundPattern826_'), da.pat.BoundPattern('_BoundPattern827_')])
PatternExpr_830 = da.pat.FreePattern('a')
_config_object = {}
import sys
from random import randint
from numpy.random import choice
import copy
import time
TIMEOUT = 1

class Proposer(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ProposerReceivedEvent_0 = []
        self._ProposerReceivedEvent_1 = []
        self._ProposerReceivedEvent_2 = []
        self._ProposerReceivedEvent_3 = []
        self._ProposerReceivedEvent_4 = []
        self._ProposerReceivedEvent_5 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_0', PatternExpr_322, sources=[PatternExpr_329], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_1', PatternExpr_357, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_2', PatternExpr_388, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_3', PatternExpr_424, sources=[PatternExpr_431], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_4', PatternExpr_471, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_5', PatternExpr_510, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, monitor, tp, nLossRate, nDelay, nWaitTime, **rest_876):
        super().setup(acceptors=acceptors, monitor=monitor, tp=tp, nLossRate=nLossRate, nDelay=nDelay, nWaitTime=nWaitTime, **rest_876)
        self._state.acceptors = acceptors
        self._state.monitor = monitor
        self._state.tp = tp
        self._state.nLossRate = nLossRate
        self._state.nDelay = nDelay
        self._state.nWaitTime = nWaitTime
        self._state.n = None
        self._state.majority = self._state.acceptors

    def run(self):
        while (not PatternExpr_515.match_iter(self._ProposerReceivedEvent_5, SELF_ID=self._id)):
            self.to_consent()

    def Loss(self):
        modifiedmajority = set()
        majorityList = list(self._state.majority)
        rndmdraw = [int(choice((0, 1), 1, p=[self._state.nLossRate, (1 - self._state.nLossRate)], replace=False)) for i in range(len(self._state.majority))]
        for (i, j) in enumerate(rndmdraw):
            if (j == 1):
                modifiedmajority.add(majorityList[i])
        return modifiedmajority

    def to_consent(self):
        self._state.n = ((0, self._id) if (self._state.n == None) else ((self._state.n[0] + 1), self._id))
        modifiedmajority = self.Loss()
        delayint = int(self._state.nDelay)
        delay = randint(0, delayint)
        time.sleep(delay)
        self.send(('prepare', self._state.n), to=modifiedmajority)
        super()._label('_st_label_317', block=False)
        n2 = None

        def ExistentialOpExpr_469():
            nonlocal n2
            for (_, _, (_ConstantPattern486_, n2)) in self._ProposerReceivedEvent_4:
                if (_ConstantPattern486_ == 'preempt'):
                    if (n2 > self._state.n):
                        return True
            return False
        _st_label_317 = 0
        self._timer_start()
        while (_st_label_317 == 0):
            _st_label_317 += 1
            if (len({a for (_, (_, _, a), (_ConstantPattern340_, _BoundPattern342_, _)) in self._ProposerReceivedEvent_0 if (_ConstantPattern340_ == 'respond') if (_BoundPattern342_ == self._state.n)}) > (len(self._state.acceptors) / 2)):
                v = self.anyof(({v for (_, _, (_ConstantPattern376_, _BoundPattern378_, (n2, v))) in self._ProposerReceivedEvent_1 if (_ConstantPattern376_ == 'respond') if (_BoundPattern378_ == self._state.n) if (n2 == max({n2 for (_, _, (_ConstantPattern405_, _BoundPattern407_, (n2, _))) in self._ProposerReceivedEvent_2 if (_ConstantPattern405_ == 'respond') if (_BoundPattern407_ == self._state.n)}))} or {randint(1, 100)}))
                responded = {a for (_, (_, _, a), (_ConstantPattern442_, _BoundPattern444_, _)) in self._ProposerReceivedEvent_3 if (_ConstantPattern442_ == 'respond') if (_BoundPattern444_ == self._state.n)}
                self.send(('accept', self._state.n, v), to=responded)
                self.send(('ProposedValue', self._state.n, v), to=self._state.monitor)
                time.sleep(self._state.nWaitTime)
                _st_label_317 += 1
            elif ExistentialOpExpr_469():
                return
                _st_label_317 += 1
            elif self._timer_expired:
                self.output('failed proposal number', self._state.n)
                time.sleep(self._state.nWaitTime)
                _st_label_317 += 1
            else:
                super()._label('_st_label_317', block=True, timeout=self._state.tp)
                _st_label_317 -= 1

    def anyof(self, s):
        return (next(iter(s)) if s else None)

class Acceptor(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._AcceptorReceivedEvent_1 = []
        self._AcceptorSentEvent_2 = []
        self._AcceptorSentEvent_3 = []
        self._AcceptorSentEvent_4 = []
        self._AcceptorSentEvent_6 = []
        self._AcceptorReceivedEvent_7 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_0', PatternExpr_558, sources=[PatternExpr_565], destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_557]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_1', PatternExpr_573, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_2', PatternExpr_603, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_3', PatternExpr_631, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_4', PatternExpr_657, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_5', PatternExpr_698, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_697]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_6', PatternExpr_711, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_7', PatternExpr_748, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, learners, monitor, nDelay, **rest_876):
        super().setup(learners=learners, monitor=monitor, nDelay=nDelay, **rest_876)
        self._state.learners = learners
        self._state.monitor = monitor
        self._state.nDelay = nDelay
        pass

    def run(self):
        super()._label('_st_label_745', block=False)
        _st_label_745 = 0
        while (_st_label_745 == 0):
            _st_label_745 += 1
            if PatternExpr_753.match_iter(self._AcceptorReceivedEvent_7, SELF_ID=self._id):
                _st_label_745 += 1
            else:
                super()._label('_st_label_745', block=True)
                _st_label_745 -= 1

    def anyof(self, s):
        return (next(iter(s)) if s else None)

    def _Acceptor_handler_557(self, n, p):
        n2 = self.anyof({n2 for (_, _, (_ConstantPattern589_, n2, _)) in self._AcceptorReceivedEvent_1 if (_ConstantPattern589_ == 'respond') if (n2 > n)})
        n2 = None

        def UniversalOpExpr_601():
            nonlocal n2
            for (_, _, (_ConstantPattern618_, n2, _)) in self._AcceptorSentEvent_2:
                if (_ConstantPattern618_ == 'respond'):
                    if (not (n > n2)):
                        return False
            return True
        if UniversalOpExpr_601():
            maxprop = self.anyof({(n, v) for (_, _, (_ConstantPattern647_, n, v)) in self._AcceptorSentEvent_3 if (_ConstantPattern647_ == 'accepted') if (n == max({n for (_, _, (_ConstantPattern672_, n, _)) in self._AcceptorSentEvent_4 if (_ConstantPattern672_ == 'accepted')}))})
            self.send(('respond', n, maxprop), to=p)
        else:
            self.send(('preempt', n2), to=p)
    _Acceptor_handler_557._labels = None
    _Acceptor_handler_557._notlabels = None

    def _Acceptor_handler_697(self, n, v):
        n2 = None

        def ExistentialOpExpr_709():
            nonlocal n2
            for (_, _, (_ConstantPattern727_, n2, _)) in self._AcceptorSentEvent_6:
                if (_ConstantPattern727_ == 'respond'):
                    if (n2 > n):
                        return True
            return False
        if (not ExistentialOpExpr_709()):
            self.send(('accepted', n, v), to=self._state.learners)
        else:
            pass
    _Acceptor_handler_697._labels = None
    _Acceptor_handler_697._notlabels = None

class Learner(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._LearnerReceivedEvent_0 = []
        self._LearnerReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_LearnerReceivedEvent_0', PatternExpr_797, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_LearnerReceivedEvent_1', PatternExpr_823, sources=[PatternExpr_830], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, monitor, tl, **rest_876):
        super().setup(acceptors=acceptors, monitor=monitor, tl=tl, **rest_876)
        self._state.acceptors = acceptors
        self._state.monitor = monitor
        self._state.tl = tl
        pass

    def run(self):
        self.learn()
        self.send(('learned',), to=self.nodeof(self._id))

    def learn(self):
        super()._label('_st_label_794', block=False)
        v = n = a = None

        def ExistentialOpExpr_795():
            nonlocal v, n, a
            for (_, _, (_ConstantPattern814_, n, v)) in self._LearnerReceivedEvent_0:
                if (_ConstantPattern814_ == 'accepted'):
                    if (len({a for (_, (_, _, a), (_ConstantPattern841_, _BoundPattern843_, _BoundPattern844_)) in self._LearnerReceivedEvent_1 if (_ConstantPattern841_ == 'accepted') if (_BoundPattern843_ == n) if (_BoundPattern844_ == v)}) > (len(self._state.acceptors) / 2)):
                        return True
            return False
        _st_label_794 = 0
        self._timer_start()
        while (_st_label_794 == 0):
            _st_label_794 += 1
            if ExistentialOpExpr_795():
                self.output('learned', n, v)
                self.send(('learned', n, v), to=self._state.monitor)
                _st_label_794 += 1
            elif self._timer_expired:
                self.output('failed learning anything')
                _st_label_794 += 1
            else:
                super()._label('_st_label_794', block=True, timeout=self._state.tl)
                _st_label_794 -= 1