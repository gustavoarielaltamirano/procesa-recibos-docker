#!/bin/bash

src_dir=/var/opt/apps/procesa-recibos-docker/procesos/finalizados/
dst_dir=/media/grupodoc/Documentos\ Compartidos/BOTSRECIBOSGG/listos

mv -f "$src_dir"/*.zip "$dst_dir"
