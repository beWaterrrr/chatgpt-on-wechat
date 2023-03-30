
""" 
本类表示聊天消息，用于对itchat和wechaty的消息进行统一的封装
ChatMessage
msg_id: 消息id
create_time: 消息创建时间

ctype: 消息类型 : ContextType
content: 消息内容, 如果是声音/图片，这里是文件路径

from_user_id: 发送者id
from_user_nickname: 发送者昵称
to_user_id: 接收者id
to_user_nickname: 接收者昵称

other_user_id: 对方的id，如果你是发送者，那这个就是接收者id，如果你是接收者，那这个就是发送者id
other_user_nickname: 同上

is_group: 是否是群消息
is_at: 是否被at

- (群消息时，一般会存在实际发送者，是群内某个成员的id和昵称，下列项仅在群消息时存在)
actual_user_id: 实际发送者id
actual_user_nickname：实际发送者昵称




_prepare_fn: 准备函数，用于准备消息的内容，比如下载图片等,
_prepared: 是否已经调用过准备函数
_rawmsg: 原始消息对象

"""
class ChatMessage(object):
    msg_id = None
    create_time = None
    
    ctype = None
    content = None
    
    from_user_id = None
    from_user_nickname = None
    to_user_id = None
    to_user_nickname = None
    other_user_id = None
    other_user_nickname = None
    
    is_group = False
    is_at = False
    actual_user_id = None
    actual_user_nickname = None

    _prepare_fn = None
    _prepared = False
    _rawmsg = None


    def __init__(self,_rawmsg):
        self._rawmsg = _rawmsg

    def prepare(self):
        if self._prepare_fn and not self._prepared:
            self._prepared = True
            self._prepare_fn()