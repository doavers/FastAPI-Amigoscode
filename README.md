# Run this
```
pip3 install fastapi "uvicorn[standard]"

uvicorn main:app --reload

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```

# Troubleshoot
## Error Message: AttributeError: module 'asyncio' has no attribute 'run'
```
pip3 uninstall uvicorn
pip3 install uvicorn==0.16.0
```
# Generated Docs
[Swagger](http://127.0.0.1:8000/docs)
[ReDocs](http://127.0.0.1:8000/redoc)

# Reference
[AmigosCode](https://youtu.be/GN6ICac3OXY)