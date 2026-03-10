import os

# Define the paths
source_static = '/home/codelabb/portfolio_repo/staticfiles'
target_static = '/home/codelabb/tanvir.codelab-by-tnv.top/static'

source_media = '/home/codelabb/portfolio_repo/media'
target_media = '/home/codelabb/tanvir.codelab-by-tnv.top/media'

try:
    # Create the static link
    if not os.path.exists(target_static):
        os.symlink(source_static, target_static)
        print("Static link created successfully!")
    else:
        print("Static link already exists.")

    # Create the media link
    if not os.path.exists(target_media):
        os.symlink(source_media, target_media)
        print("Media link created successfully!")
except Exception as e:
    print(f"Error: {e}")