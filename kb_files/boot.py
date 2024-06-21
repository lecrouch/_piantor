import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "PIANTOR_L"
# m.label = "PIANTOR_C_L"
# m.label = "PIANTOR_R"
# m.label = "PIANTOR_C_R"

storage.remount("/", readonly=True)

storage.enable_usb_drive()
