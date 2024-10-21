import os
import shutil

# 創毽子資料夾
def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)

    # 如果沒有子資料夾的話，建立
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


# 根據檔案類型，將指定資料夾中的檔案放到子資料夾中
def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # 抓出副檔名
            file_extension = filename.split('.')[-1].lower()
            # 檢查檔案有沒有副檔名
            if file_extension:
                # 利用副檔名，確定子資料夾名稱
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                # 取得檔案路徑
                file_path = os.path.join(folder_path, filename)
                # 移動檔案到指定子資料夾
                shutil.move(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}/")


if __name__ == "__main__":
    print("桌面文件整理")
    folder_path = (" ")     # 輸入要整理的資料夾
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("整理完成。")
    else:
        print("沒有找到文件，請重新確認路徑是否正確。")
