```

Date:   26 Dec 2021
EDITED V1  :   26 Dec 2021
EDITED V2  :   
Descriptions: [RFC6910]
MAJOR RELEASE   :   
```

# SIP :RFC
 1.  RFC1889 - RTP & QoS
 2.  RFC2325 - RTPSP (Controlling)
 3.  RFC3015 - Media Gateway Control Protocol (For PSTN)
 4.  RFC2327 - Session Description Protocol (SDP)
 5.  RFC3261 - Header Details ############### https://datatracker.ietf.org/doc/html/rfc3261#section-20


## RFC6910 Completion of Calls for the Session Initiation Protocol (SIP)

```

   The "completion of calls" feature defined in this specification
   allows the caller of a failed call to be notified when the callee
   becomes available to receive a call.
   ```
## SIP URI: (HTTP-like request/response transaction model)
        sip:user@host_name


        Via:    contains the address of #local_host# at which "NEC" is
                expecting to receive responses to this request.  It also contains a
                branch parameter that identifies this transaction

    (a)    INVITE sip:TO_EXT@REMOTE_SERVER;user=phone;transport=UDP;tgrp=1;trunk-context=xxx.test.com SIP/2.0\r\n"

    (b)    Via: SIP/2.0/UDP LOCAL_SERVER:5060;branch=z9hG4bK-{}\r\n


                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                quoted-pair     =       ("\" text) / obs-qp

                Where any quoted-pair appears, it is to be interpreted as the text
                character alone.  That is to say, the "\" character that appears as
                part of a quoted-pair is semantically "invisible".
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

       To:     contains a display name (#In this only ext  number#) and a SIP or SIPS URI
                (sip:name/number@remote SIP_SERVER) towards which the request was originally
                directed.  Display names are described in RFC 2822

       From:   also contains a display name (#here will use Caller's ext ) and a SIP or SIPS URI
                (sip:caller@local_host) that indicate the originator of the request.
                This header field also has a tag parameter containing a random string
                (1928301774) that was added to the URI by the softphone.  It is used
                for identification purposes

      Call-ID: contains a globally unique identifier for this call,
                generated by the combination of a random string and the softphone's
                host name or IP address.

                    The combination of the To tag, From tag,
                    and Call-ID completely defines a peer-to-peer SIP relationship
                    between NEC and MITEL and is referred to as a dialog.

      CSeq:   or Command Sequence contains an integer and a method name.  The
                CSeq number is incremented for each new request within a dialog and
                is a traditional sequence number

      Contact:    contains a SIP or SIPS URI that represents a direct route to
                    contact NEC, usually composed of a username at a fully qualified
                    domain name (FQDN).  While an FQDN is preferred, many end systems do
                    not have registered domain names, so IP addresses are permitted.

                        While the Via header field tells other elements where to send the
                        response, the Contact header field tells other elements where to send
                        future requests.


        100 Trying:

                    This response indicates that the request has been received by the
                    next-hop server and that some unspecified action is being taken on
                    behalf of this call (for example, a database is being consulted).
                    This response, like all other provisional responses, stops
                    retransmissions of an INVITE by a UAC.  The 100 (Trying) response is
                    different from other provisional responses, in that it is never
                    forwarded upstream by a stateful proxy.
        180 Ringing:

                    The UA receiving the INVITE is trying to alert the user.  This
                    response MAY be used to initiate local ringback.

        200 OK:

                    The request has succeeded.  The information returned with the
                    response depends on the method used in the request.


        486 Busy Here:

                    The callee's end system was contacted successfully, but the callee is
                    currently not willing or able to take additional calls at this end
                    system.  The response MAY indicate a better time to call in the
                    Retry-After header field.  The user could also be available

                    elsewhere, such as through a voice mail service.  Status 600 (Busy
                    Everywhere) SHOULD be used if the client knows that no other end
                    system will be able to accept this call.


