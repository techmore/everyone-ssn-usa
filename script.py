import os
import itertools

def generate_and_save_batch(start, end, file_name):
    combinations = []

    for a in range(start, end + 1):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                combination = f"{str(a).zfill(2)}{str(b).zfill(1)}-{str(c).zfill(2)}-{str(d).zfill(1)}{str(e).zfill(1)}{str(f).zfill(1)}{str(g).zfill(1)}"
                                combinations.append(combination)

    with open(file_name, 'w') as f:
        f.write("\n".join(combinations))
    
    print(f"Batch saved to {file_name}")

def generate_batches():
    folder_path = "./all-ssn-batches"
    os.makedirs(folder_path, exist_ok=True)

    batch_ranges = [
        {'start': 0, 'end': 3, 'file_name': f"{folder_path}/batch-a.txt"},
        {'start': 4, 'end': 7, 'file_name': f"{folder_path}/batch-b.txt"},
        {'start': 8, 'end': 11, 'file_name': f"{folder_path}/batch-c.txt"},
        {'start': 12, 'end': 15, 'file_name': f"{folder_path}/batch-d.txt"},
        {'start': 16, 'end': 19, 'file_name': f"{folder_path}/batch-e.txt"},
        {'start': 20, 'end': 23, 'file_name': f"{folder_path}/batch-f.txt"},
        {'start': 24, 'end': 27, 'file_name': f"{folder_path}/batch-g.txt"},
        {'start': 28, 'end': 31, 'file_name': f"{folder_path}/batch-h.txt"},
        {'start': 32, 'end': 35, 'file_name': f"{folder_path}/batch-i.txt"},
        {'start': 36, 'end': 39, 'file_name': f"{folder_path}/batch-j.txt"},
        {'start': 40, 'end': 43, 'file_name': f"{folder_path}/batch-k.txt"},
        {'start': 44, 'end': 47, 'file_name': f"{folder_path}/batch-l.txt"},
        {'start': 48, 'end': 51, 'file_name': f"{folder_path}/batch-m.txt"},
        {'start': 52, 'end': 55, 'file_name': f"{folder_path}/batch-n.txt"},
        {'start': 56, 'end': 59, 'file_name': f"{folder_path}/batch-o.txt"},
        {'start': 60, 'end': 63, 'file_name': f"{folder_path}/batch-p.txt"},
        {'start': 64, 'end': 67, 'file_name': f"{folder_path}/batch-q.txt"},
        {'start': 68, 'end': 71, 'file_name': f"{folder_path}/batch-r.txt"},
        {'start': 72, 'end': 75, 'file_name': f"{folder_path}/batch-s.txt"},
        {'start': 76, 'end': 79, 'file_name': f"{folder_path}/batch-t.txt"},
        {'start': 80, 'end': 83, 'file_name': f"{folder_path}/batch-u.txt"},
        {'start': 84, 'end': 87, 'file_name': f"{folder_path}/batch-v.txt"},
        {'start': 88, 'end': 91, 'file_name': f"{folder_path}/batch-w.txt"},
        {'start': 92, 'end': 95, 'file_name': f"{folder_path}/batch-x.txt"},
        {'start': 96, 'end': 99, 'file_name': f"{folder_path}/batch-y.txt"},
        {'start': 100, 'end': 103, 'file_name': f"{folder_path}/batch-z.txt"},
    ]

    for batch in batch_ranges:
        generate_and_save_batch(batch['start'], batch['end'], batch['file_name'])

if __name__ == "__main__":
    generate_batches()
