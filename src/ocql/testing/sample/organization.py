from zope.interface import implements
from zope.app.container.btree import BTreeContainer

from ocql.testing.sample.interfaces import IOrganization
from ocql.testing.sample.interfaces import IOrganizationContained, IOrganizationContainer

class Organization(BTreeContainer):
    """A simple implementation of an organization .

    Make sure that the ``Organization`` implements the ``IOrganization`` interface:


    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IOrganization, Organization)
    True

    Here is an example of changing the name of the organization:

    >>> organization = Organization()
    >>> organization.name
    u''

    >>> organization.name = u'Organization Name'
    >>> organization.name
    u'Organization Name'
    """
    implements(IOrganization, IOrganizationContained, IOrganizationContainer)

    # See google.interfaces.IOrganization
    name = u''

    def __init__(self, name=u''):
        self.name = name

    def __repr__(self):
        return "%s <%s>" % (self.__class__.__name__, self.name)
