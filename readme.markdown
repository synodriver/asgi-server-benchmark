# ASGI-Server Benchmark

## Servers
- [uvicorn](https://github.com/encode/uvicorn) with gunicorn to manage process
- [hypercorn with gunicorn](https://gitlab.com/synodriver/hypercorn/-/tree/nonecorn) to manage process
- [nginx-unit](https://github.com/nginx/unit)

> Note: To make it fair for hypercorn, I made a [patch](https://gitlab.com/synodriver/hypercorn/-/tree/nonecorn) to it and now hypercorn can run
> as gunicorn's worker, since the author of hypercorn seems to have different priorities currently, 
> Before those pr are merged, you can just
> ```pip install nonecorn==0.11.2rc5```to test, I fixed some bugs, merged some pr for hypercorn and added some features(like gunicorn worker) 
> in that fork.

## Start

- uvicorn: ```python -m gunicorn -c gunicornconfig.py```
- hypercorn ```python -m gunicorn -c hypercornconfig.py```
- nginx-unit ```curl -X PUT --data-binary @unitconfig.json --unix-socket 
       /path/to/control.unit.sock http://localhost/config```