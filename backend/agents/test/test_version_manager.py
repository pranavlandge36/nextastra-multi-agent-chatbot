from agents.version_manager import (
    save_version,
    get_current_file,
    get_versions
)


save_version("outputs/test_v1.pptx")
save_version("outputs/test_v2.pptx")

print("CURRENT:")
print(get_current_file())

print("\nVERSIONS:")
print(get_versions())