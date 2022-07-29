# Databricks notebook source
mount_file_names = [""]
storageAccountName = ""
storageAccountAccessKey = ""
len(mount_file_names)

# COMMAND ----------

for container in mount_file_names: 
    mount_point = "/mnt/{}/".format(container)
    print(mount_point)

# COMMAND ----------

for blobContainerName in mount_file_names:
    if not any(mount.mountPoint == "/mnt/" for mount in dbutils.fs.mounts()):
        dbutils.fs.mount(
            source = "wasbs://{}@{}.blob.core.windows.net".format(blobContainerName, storageAccountName),
            mount_point = "/mnt/{}/".format(blobContainerName),
            extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
        )

# COMMAND ----------

import os
os.listdir("/dbfs/mnt/")

# COMMAND ----------


