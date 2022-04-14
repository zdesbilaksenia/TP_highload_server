# Python-prefork веб-сервер

# Функциональное тестирование
```commandline
ksenia@Ksenia:~/TP_highload_server$ ./httptest.py
test_directory_index (__main__.HttpServer)
directory index file exists ... ok
test_document_root_escaping (__main__.HttpServer)
document root escaping forbidden ... ok
test_empty_request (__main__.HttpServer)
Send empty line ... ok
test_file_in_nested_folders (__main__.HttpServer)
file located in nested folders ... ok
test_file_not_found (__main__.HttpServer)
absent file returns 404 ... ok
test_file_type_css (__main__.HttpServer)
Content-Type for .css ... ok
test_file_type_gif (__main__.HttpServer)
Content-Type for .gif ... ok
test_file_type_html (__main__.HttpServer)
Content-Type for .html ... ok
test_file_type_jpeg (__main__.HttpServer)
Content-Type for .jpeg ... ok
test_file_type_jpg (__main__.HttpServer)
Content-Type for .jpg ... ok
test_file_type_js (__main__.HttpServer)
Content-Type for .js ... ok
test_file_type_png (__main__.HttpServer)
Content-Type for .png ... ok
test_file_type_swf (__main__.HttpServer)
Content-Type for .swf ... ok
test_file_urlencoded (__main__.HttpServer)
urlencoded filename ... ok
test_file_with_dot_in_name (__main__.HttpServer)
file with two dots in name ... ok
test_file_with_query_string (__main__.HttpServer)
query string with get params ... ok
test_file_with_slash_after_filename (__main__.HttpServer)
slash after filename ... ok
test_file_with_spaces (__main__.HttpServer)
filename with spaces ... ok
test_head_method (__main__.HttpServer)
head method support ... ok
test_index_not_found (__main__.HttpServer)
directory index file absent ... ok
test_large_file (__main__.HttpServer)
large file downloaded correctly ... ok
test_post_method (__main__.HttpServer)
post method forbidden ... ok
test_request_without_two_newlines (__main__.HttpServer)
Send GET without to newlines ... ok
test_server_header (__main__.HttpServer)
Server header exists ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.032s

OK
```

# Нагрузочное тестирование в сравнении с Nginx
### Веб-сервер
```commandline
ksenia@Ksenia:~/TP_highload_server$ ab -c 100 -n 1000 http://localhost:80/httptest/wikipedia_russia.html
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        My
Server Hostname:        localhost
Server Port:            80

Document Path:          /httptest/wikipedia_russia.html
Document Length:        954824 bytes

Concurrency Level:      100
Time taken for tests:   0.742 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      954972000 bytes
HTML transferred:       954824000 bytes
Requests per second:    1348.48 [#/sec] (mean)
Time per request:       74.157 [ms] (mean)
Time per request:       0.742 [ms] (mean, across all concurrent requests)
Transfer rate:          1257583.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.9      1       5
Processing:     8   70  16.2     72     119
Waiting:        1    7  10.6      3      55
Total:         11   71  15.9     73     122

Percentage of the requests served within a certain time (ms)
  50%     73
  66%     74
  75%     75
  80%     76
  90%     80
  95%     99
  98%    105
  99%    107
 100%    122 (longest request)

```
### Nginx
```commandline
ksenia@Ksenia:/etc/nginx$ ab -c 100 -n 1000 http://localhost:8081/httptest/wikipedia_russia.html
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.18.0
Server Hostname:        localhost
Server Port:            8081

Document Path:          /httptest/wikipedia_russia.html
Document Length:        954824 bytes

Concurrency Level:      100
Time taken for tests:   0.265 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      955071000 bytes
HTML transferred:       954824000 bytes
Requests per second:    3774.13 [#/sec] (mean)
Time per request:       26.496 [ms] (mean)
Time per request:       0.265 [ms] (mean, across all concurrent requests)
Transfer rate:          3520076.55 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.4      0       3
Processing:    14   25   3.2     25      38
Waiting:        0    1   1.5      0       9
Total:         15   26   3.3     26      39
ERROR: The median and mean for the initial connection time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%     26
  66%     26
  75%     26
  80%     26
  90%     27
  95%     34
  98%     38
  99%     38
 100%     39 (longest request)

```