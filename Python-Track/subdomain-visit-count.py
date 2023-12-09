class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = defaultdict(int)
        for domains in cpdomains:
            cost, domain = domains.split()
            d = domain.split('.')
            for i in range(len(d)):
                result['.'.join(d[i:])] += int(cost)
        res = []
        for key, value in result.items():
            res.append(str(value) + " " + key)
        return res
        