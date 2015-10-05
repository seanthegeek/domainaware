# DomainAware
 *Remain aware with DomainAware*

A [dnstwist](https://github.com/elceef/dnstwist) and/or [URLCrazy](http://www.morningstarsecurity.com/research/urlcrazy)
wrapper for emailing security staff when possible typo sqatting/spear phishing domains have been registered

## Dependencies

- Python 3
- Ruby
- [Requests](https://pypi.python.org/pypi/requests/)
- [URLCrazy](http://www.morningstarsecurity.com/research/urlcrazy)
- [dnstwist](https://github.com/seanthegeek/dnstwist/tree/patch-1)
  - [DNS toolkit for Python](https://pypi.python.org/pypi/dnspython)
  - [Python GeoIP](https://pypi.python.org/pypi/GeoIP/)
    - [MaxMind Legacy Country GeoIP Database](https://dev.maxmind.com/geoip/legacy/install/country/)

Please note: There is currently [a bug](https://github.com/elceef/dnstwist/pull/27) in dnstwist that causes it to generate invalid CSV data, breaking DomainAware.
Please use the version from [my branch](https://github.com/seanthegeek/dnstwist/tree/patch-1) until the patch is merged.

## Use

After installing the above dependencies, edit the `settings.cfg` file:

- Set the path to dnstwist and URLCrazy
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

DomainAware was inspired is inspired by Mike Saunders' [CrazyParser](https://github.com/hardwaterhacker/CrazyParser).
It started as a fork, but by the time I made all the changes I wanted, I realized that I had almost completely different
code, with a similar concept. The main differences are:

- Python coding standards are followed
- Configuration in a file, rather than within the code
- Email notification if `knowndomains.csv` has not been updated since the last run 
- NS, MX, A, and AAAA DNS records, and country and fuzzer information are included in the results
- Domain information is stored in memory rather than temporary files
- Integration with the DomainTools WHOIS APIs
