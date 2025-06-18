apiVersion: v1
kind: Service
metadata:
 labels:
 k8s-app: k8s_python_demo_code
 name: hellopy
spec:
 type: NodePort
 ports:
 — port: 4025
 selector:
 k8s-app: k8s_python_demo_code
