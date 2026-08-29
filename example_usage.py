from client import ColumnarEmbeddedVectorAnalyticalStoreClient

def main():
    client = ColumnarEmbeddedVectorAnalyticalStoreClient()
    res = client.execute_analytical_vector_scan('sec_financial_filings_10k')
    print('Columnar Vector Scan: ' + res['analytical_scan_id'] + ' | Collection: ' + res['collection'])
    print('Rows Scanned: ' + str(res['columnar_rows_scanned']) + ' -> Filtered: ' + str(res['predicate_pushdown_filtered_count']))
    print('Top K Matches: ' + str(res['cosine_top_k_results_count']) + ' (Latency: ' + str(res['in_process_query_latency_ms']) + 'ms)')
    print('Parquet Persisted: ' + str(res['duckdb_sqlite_parquet_persisted']))

if __name__ == '__main__':
    main()
