# -*- coding: utf-8 -*-
import multiprocessing

wsgi_app = "main:app"
bind = '0.0.0.0:9000'
timeout = 30
workers = 2

worker_class = "hypercorn.workers.HypercornUvloopWorker"

worker_connections = 10000

loglever = "debug"
accesslog = "access.log"

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "error.log"
