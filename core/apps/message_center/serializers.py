#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/17 
=================================================='''

from rest_framework import serializers
from message_center.models import UserNotificationConfig

__all__ = ["UserNotificationConfigSerializer"]


class UserNotificationConfigSerializer(serializers.ModelSerializer):
    vars = serializers.DictField(required=False)

    class Meta:
        model = UserNotificationConfig
        fields = [
            'id', 'user_id', 'type', 'vars'
        ]
