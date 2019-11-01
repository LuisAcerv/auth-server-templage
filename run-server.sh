
#!/bin/bash

serve(){
    gunicorn --worker-class eventlet --log-level debug -b 0.0.0.0:5000 app.app:app --reload             
}

serve

