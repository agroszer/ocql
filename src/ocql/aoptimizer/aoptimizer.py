# -*- coding: UTF-8 -*-

""" Optimizing will be done later,
at the moment this is just a stub returning it's input

$Id$
"""
from zope.component import adapts
from zope.interface import implements
#from zope.security.proxy import removeSecurityProxy
from zope.interface import directlyProvidedBy
from zope.interface import directlyProvides

from ocql.interfaces import IAlgebraOptimizer

from ocql.interfaces import IAlgebraObjectHead
from ocql.interfaces import IOptimizedAlgebraObject
from ocql.rewriter.algebra import BaseAlgebra

def addMarkerIF(obj, marker):
    #obj = removeSecurityProxy(obj)
    if not marker.providedBy(obj):
        directlyProvides(obj, directlyProvidedBy(obj), marker)

def visit(algebra):
    if isinstance(algebra , BaseAlgebra):
        for child in algebra.children:
            visit(child)
    print str(algebra)

class AlgebraOptimizer(object):
    implements(IAlgebraOptimizer)
    adapts(IAlgebraObjectHead)

    def __init__(self, context):
        self.context = context
        #self.db = db

    def __call__(self):
        addMarkerIF(self.context, IOptimizedAlgebraObject)
        visit(self.context.tree)
        return self.context
    


