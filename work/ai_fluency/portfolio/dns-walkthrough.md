# How a website address finds the page
AI-assisted study draft for PF-04. Student review is still needed.

DNS means Domain Name System. It helps turn a website name into a network
address. You remember the name; the computer needs the address to connect.
DNS finds the host. It does not carry the web page itself.

When you type a website address, your browser or computer may already have a
recent DNS answer saved. If not, it asks a resolver. The resolver is the service
that looks up an answer for you. If its own saved answer is missing, it follows
the DNS system toward the nameservers responsible for the requested name.

A nameserver holds DNS records. An authoritative nameserver gives the official
DNS answer for the names it manages. A record is a particular instruction or
answer. An A record gives an IPv4 address. An AAAA record gives an IPv6 address.
The resolver returns the result to your computer and may save it for a limited
time. This caching makes later lookups quicker, but means changes may not
appear everywhere immediately.

A CNAME record is an alias: it points one name to another name, rather than
directly to an IP address. For example, a future `www` subdomain could point to
a hosting name. The lookup then follows that target to find an address. This
is not the same as redirecting the visitor to a different web-page address.
The host still needs to recognize the requested domain.

After finding an address, the browser connects to the host. With HTTPS, it
checks the site's certificate and sets up an encrypted connection. It requests
the page, and the host returns HTML, CSS, JavaScript and other assets. The
browser uses those files to display the page. DNS lookup and page delivery
are different steps.

This portfolio uses the address supplied by its host. No custom domain was
bought, and no personal CNAME record was configured. For a future custom domain,
follow the host's exact DNS instructions rather than copying example values.

References checked November 11, 2026:
- https://www.cloudflare.com/learning/dns/what-is-dns/
- https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/
