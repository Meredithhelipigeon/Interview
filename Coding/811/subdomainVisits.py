class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_to_counts = {}
        for cp in cpdomains:
            count, domains = cp.split(" ")
            count = int(count)
            domains = reversed(domains.split("."))
            cur = []
            for d in domains:
                cur.append(d)
                curDomainString = ".".join(reversed(cur))
                if curDomainString in domains_to_counts:
                    domains_to_counts[curDomainString] += count
                else:
                    domains_to_counts[curDomainString] = count
        ret = []
        for domain_key in domains_to_counts:
            retDomainCount =  str(domains_to_counts[domain_key]) + " " + domain_key 
            ret.append(retDomainCount)
        return ret

class Solution2:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_to_counts = {}
        for cp in cpdomains:
            count, domains = cp.split(" ")
            count = int(count)
            domains = domains.split(".")
            for i in range(len(domains)):
                curDomainString = ".".join(domains[i:])
                if curDomainString in domains_to_counts:
                    domains_to_counts[curDomainString] += count
                else:
                    domains_to_counts[curDomainString] = count
        ret = []
        for domain_key in domains_to_counts:
            retDomainCount =  str(domains_to_counts[domain_key]) + " " + domain_key 
            ret.append(retDomainCount)
        return ret
