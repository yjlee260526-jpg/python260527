import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
downloads_folder = r"C:\Users\student\Downloads"

# 파일 분류 정보
file_mapping = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 다운로드 폴더 객체 생성
downloads_path = Path(downloads_folder)

# 1. 목표 폴더 생성 (없으면 생성)
for folder_name in file_mapping.keys():
    target_folder = downloads_path / folder_name
    target_folder.mkdir(exist_ok=True)
    print(f"폴더 생성/확인: {target_folder}")

# 2. 파일 이동
for folder_name, patterns in file_mapping.items():
    target_folder = downloads_path / folder_name
    
    for pattern in patterns:
        # glob 패턴으로 파일 찾기
        for file_path in downloads_path.glob(pattern):
            if file_path.is_file():
                # 파일 이동
                destination = target_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"이동됨: {file_path.name} → {folder_name}/")

print("파일 정렬 완료!")