from fec_wrapper import FECDataFetcher

fetcher = FECDataFetcher()
candidates = fetcher.get_candidates()
print(candidates)

