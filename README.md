# A patch to python requests 
Thanks to passos's [reply](https://github.com/passos) at [https://github.com/requests/requests/issues/1604](https://github.com/requests/requests/issues/1604) 
## Quick start
Test in python2.7, not sure if it works well in other version.

```shell
cd /tmp/
git clone https://github.com/fiht/reqeusts_patch_example
cd reqeusts_patch_example
virtulenv /tmp/venv
source /tmp/venv/bin/active
pip install -r requirements.txt
python main.py
``` 
The output should be 
```html
BEFORE PATCH:
****************************************************************************************************

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta name="description" content="É½¶«´óÑ§,É½´ó,É½¶«´óÑ§¹Ù·½ÍøÕ¾,É½´ó¹ÙÍø,SDU" />
<meta name="keywords" content="É½¶«´óÑ§,É½´ó,É½¶«´óÑ§¹Ù·½ÍøÕ¾,É½´ó¹ÙÍø,SDU" />
<meta name="Copyright" content="Copyright (c) 2010 www.sdu.edu.cn All Rights Reserv
****************************************************************************************************


AFTER PATCH:
****************************************************************************************************

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta name="description" content="山东大学,山大,山东大学官方网站,山大官网,SDU" />
<meta name="keywords" content="山东大学,山大,山东大学官方网站,山大官网,SDU" />
<meta name="Copyright" content="Copyright (c) 2010 www.sdu.edu.cn All Rights Reserved." />
<title>欢迎访问山东大学主页</title>

****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
```
