#!/bin/bash
kubeadm init \
--apiserver-advertise-address=$1 \
--kubernetes-version v1.20.15 \
--service-cidr=10.96.0.0/12 \
--pod-network-cidr=10.244.0.0/16
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml > /dev/null