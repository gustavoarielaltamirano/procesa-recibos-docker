#!/bin/bash

src_dir="/media/grupodoc/Documentos Compartidos/BOTSRECIBOSGG"
dst_dir="/var/opt/apps/procesa-recibos-docker/resultados"

cp -r "$src_dir/*.zip" "$dst_dir"
