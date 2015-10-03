# domainaware
 *Remain aware with domainaware*

A [dnstwist](https://github.com/elceef/dnstwist) wrapper for emailing security staff when possible typo sqatting/spear 
phishing domains have been registered

## Dependencies

- Python 2.7
- [unicodecsv](https://pypi.python.org/pypi/unicodecsv)
- [Requests: HTTP for Humans](http://www.python-requests.org/)
- [dnstwist](https://github.com/elceef/dnstwist)
  - [DNS toolkit for Python](http://www.dnspython.org/)
  - [Python GeoIP](https://pypi.python.org/pypi/GeoIP/)
    - [MaxMind Legacy Country GeoIP Database](https://dev.maxmind.com/geoip/legacy/install/country/)

## Use

After installing the above dependencies, edit the `settings.cfg` file:

- Set the path to dnstwist
- Configure the email settings

If you have a subscription to the 
[DomainTools WHOIS APIs](https://www.domaintools.com/products/api-integration/pricing/), you can add your credentials to
include the registrar name, registrant name, creation date, updated date, and expiration date in the domainaware
results. Both the plain WHOIS APIs and the parsed WHOIS APIs provide this same basic information, but you might have 
access to one and not the other, with different URLs, so specify the flavor using the `parsed` parsed setting.

Determine the critical domains the critical domains that you would like to monitor; for example, key brands.
Add those domains to `mydomains.csv`, one per line. Include any and all ligament TLD variants, even if they are not
actually used at all, except typo variations.

Add any other domains you or your organisation may own under the `Domain` header in `knowndomains.csv`, including any 
owned typo domains. Add a reason like `Valid` for each domain. The `Reason` field is for the use of humans, and is not 
used by the script. The file is simply used by the analyst to keep track of all domains that have been reviewed.

Run the script for the first time:

    $ ./domainaware --email

Open `output.csv`. Add all of the domains to `knowndomains.csv`, then review each domain to see if it's valid, or 
if it's something you should add alerts and/or blocks for with your security controls. The domains are not automatically
added so that that human review is required. If the script detects that that there ate domains from its last run that 
are not in `knowndomains.csv`, it will send an email notice of this and exit, so that analysts have a chance to review
all domains before alerts for new ones are issued.

It is recommended to run the script once a day, either manually, or via cron. 

For recording and tracking threat information, check out the [CRITs](https://github.com/crits/crits) project.

If you need reliable external SMTP service, [Mandrill](https://www.mandrill.com/) from MailChimp 
provides low-cost service for transactional mail.

Check for and download new versions of dnstwist regularly.

## Background

domainaware was inspired is inspired by Mike Saunders' [CrazyParser](https://github.com/hardwaterhacker/CrazyParser).
It started as a fork, but by the time I made all the changes I wanted, I realized that I had almost completely different
code, with a similar concept. The main differences are:

- `urlcrazy` is not used, because it generates domains which may not be registered
- Python coding standards are followed
- Configuration in a file, rather than within the code
- Email notification if `knowndomains.csv` has not been updated since the last run 
- NS, MX, A, AAAA DNS records, and country and fuzzer information from dnstwist are included in the results
- Domain information is stored in memory rather than temporary files
- Integration with the DomainTools WHOIS APIs
