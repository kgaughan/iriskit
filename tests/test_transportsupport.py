from iriskit import transportsupport as ts
from iriskit import lwz, namespaces
from lxml.etree import tostring


def test_build_version_info():
    text = tostring(ts.build_version_info({}))
    assert text == '<versions xmlns="urn:ietf:params:xml:ns:iris-transport"/>'

    text = tostring(ts.build_version_info({lwz.PROTOCOL_ID: []}))
    assert text == (
        '<versions xmlns="urn:ietf:params:xml:ns:iris-transport">' +
        '<transferProtocol protocolId="iris.lwz1">' +
        '<application protocolId="urn:ietf:params:xml:ns:iris-transport"/>' +
        '</transferProtocol>' +
        '</versions>')

    protocols = {
        lwz.PROTOCOL_ID: [
            namespaces.DREG,
            namespaces.DCHK,
        ]
    }
    text = tostring(ts.build_version_info(protocols))
    assert text == (
        '<versions xmlns="urn:ietf:params:xml:ns:iris-transport">' +
        '<transferProtocol protocolId="iris.lwz1">' +
        '<application protocolId="urn:ietf:params:xml:ns:iris-transport">' +
        '<dataModel protocolId="urn:ietf:params:xml:ns:dreg1"/>' +
        '<dataModel protocolId="urn:ietf:params:xml:ns:dchk1"/>' +
        '</application>' + 
        '</transferProtocol>' +
        '</versions>')
