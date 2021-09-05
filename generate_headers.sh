ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

headers=
libs=
set -e

cybertron_api="cybertron_api"

mkdir -p $cybertron_api/{incr,libs}

pushd bazel-cybertron
  headeres=()
  find modules/ -name "*.h" -print0 > cli_header_list
  while IFS= read -r -d $'\0'; do
    headers+=("$REPLY")
  done < cli_header_list
  echo "find ${#headers[*]} headers"
 
  for f in ${headers[@]}; do
    # echo "file: $f"
    cp --parents $f "$ROOT/$cybertron_api/incr"
  done

popd


pushd bazel-bin
  libs=()
  find . -type f -or -type l -name "*.so" -print0 > cli_so_list
  while IFS= read -r -d $'\0'; do
    libs+=("$REPLY")
  done < cli_so_list
  echo "find ${#libs[*]} shared libraries"

  for f in ${libs[@]}; do
    # echo "file : $f"
    sudo cp --parents $f "$ROOT/$cybertron_api/libs/"
  done

popd

