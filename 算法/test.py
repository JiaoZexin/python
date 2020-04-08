#======================= Global Settings =====================================

[global]

# ----------------------- Network Related Options -------------------------

        workgroup = WORKGROUP
        server string = David Samba Server Version %v
        netbios name = DavidSamba

# --------------------------- Logging Options -----------------------------
        log file = /var/log/samba/log.%m

# ----------------------- Standalone Server Options ------------------------
#
# Scurity can be set to user, share(deprecated) or server(deprecated)

        security = user                                   //用户级别，由提供服务的Samba服务器负责检查账户和密码

#============================ Share Definitions ==============================


[public]
        comment = Public Stuff
        path = /share
        public = yes

[ts]                                                      //ts 组目录，只允许ts组成员访问
        comment = TS
        path = /ts
        valid users = @ts   #将ts属组的用户加入