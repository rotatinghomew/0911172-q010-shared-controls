from collections import defaultdict

def summarize(records, group_key, value_key):
    groups = defaultdict(list)
    for row in records:
        value = row.get(value_key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            groups[str(row.get(group_key, "unknown"))].append(value)
    return {key: {"n": len(values), "mean": sum(values) / len(values)}
            for key, values in sorted(groups.items()) if values}
