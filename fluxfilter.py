#!/opt/fluxfilter/bin/python3

import re
import miniflux

SITES = {
    "https://www.thepinballnetwork.net": [r"^The Pinball Show Ep",r"^The Puppet Palz Ep",r"^Top 3 With Orby Ep",r"TPS Midweek Ep",r"^\Silverball Stories Ep",],
    "http://512pixels.net": [r"^sponsor: ", r" #\d+: ",],
}

SITE = "{{ miniflux.api.url }}"
USER = "{{ miniflux.api.user }}"
PASSWORD = "{{ miniflux.api.password }}"

client = miniflux.Client(SITE, USER, PASSWORD)
res = client.get_entries(status="unread", direction="desc", limit=100)

ids = []

for e in res["entries"]:
    for site, rules in SITES.items():
        if e["feed"]["site_url"] == site:
            for rule in rules:
                if re.search(rule, e["title"], re.IGNORECASE):
                    ids.append(e["id"])
                    print(f"{site} /{rule}/:", e["title"])

if len(ids):
    client.update_entries(ids, "read")
