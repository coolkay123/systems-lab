# DNS, TCP, TLS, and HTTP

## First planned experiment: trace one URL

Follow one request through the stack and save sanitized evidence:

1. Resolve the hostname with `dig`.
2. Inspect connection and protocol negotiation with `curl -v`.
3. Inspect the certificate with `openssl s_client`.
4. Capture your own request in Wireshark.
5. Explain what DNS, TCP or QUIC, TLS, and HTTP each contributed.

Do not commit authentication headers, cookies, private hostnames, or unfiltered
packet captures. Prefer short redacted text traces.

