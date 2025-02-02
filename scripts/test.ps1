bombardier --fasthttp -c 200 -d 60s http://localhost:3000/
bombardier --fasthttp -c 200 -d 60s http://localhost:3000/id/1?name=bun
bombardier --fasthttp -c 200 -d 60s -m POST -H 'Content-Type: application/json' -f ./body.json http://localhost:3000/json
Stop-Process -Name "bun"
echo "Done"
echo "a"

bombardier --fasthttp -c 200 -d 60s http://localhost:3001/
bombardier --fasthttp -c 200 -d 60s http://localhost:3001/id/1?name=rst
bombardier --fasthttp -c 200 -d 60s -m POST -H 'Content-Type: application/json' -f ./body.json http://localhost:3001/json
Stop-Process -Name "actix"

echo "Done"