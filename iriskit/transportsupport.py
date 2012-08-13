"""
Common IRIS transport support code.
"""

from lxml.builder import ElementMaker
from iriskit import namespaces


E = ElementMaker(
    namespace=namespaces.IRIS_TRANSPORT,
    nsmap={None: namespaces.IRIS_TRANSPORT})


def build_version_info(protocols):
    """
    Takes a dict mapping protocol IDs to lists of data models namespaces.
    """
    protocol_elements = []
    for protocol, models in protocols.iteritems():
        application = E.application(
            *[E.dataModel(protocolId=model) for model in models],
            protocolId=namespaces.IRIS_TRANSPORT)
        protocol_elements.append(
            E.transferProtocol(application, protocolId=protocol))
    return E.versions(*protocol_elements)
