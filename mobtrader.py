#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#______  ___       ______  ________                _________#             
#___   |/  /______ ___  /_ ___  __/______________ _______  /_____ ________#
#__  /|_/ / _  __ \__  __ \__  /   __  ___/_  __ `/_  __  / _  _ \__  ___/#
#_  /  / /  / /_/ /_  /_/ /_  /    _  /    / /_/ / / /_/ /  /  __/_  /# 
#/_/  /_/   \____/ /_.___/ /_/     /_/     \__,_/  \__,_/   \___/ /_/# 
#FULL MHI V 1.0 - Contato: +55 (11) 9 7615-9233#

import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
