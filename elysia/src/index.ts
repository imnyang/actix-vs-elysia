import { Elysia, t } from 'elysia'
import fs from 'fs';
import path from 'path';

const app = new Elysia()
  .get('/', 'Hi')
  .get('/id/:id', (c) => {
    c.set.headers['x-powered-by'] = 'benchmark'

    return `${c.params.id} ${c.query.name}`
  })
  .post('/json', (c) => c.body, {
    type: 'json'
  })
  .listen(3000)
;

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);