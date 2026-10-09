   # Learnings

   ## Week 1
   - Week 1 done: skeleton, CI, protected main

   1. uvicorn is the server, so listens and writes and serves. FsatAPI routes each request by matching the request to the appropriate function
   2. CIs machine: clean install that sees only whats on GIT, not your laptop
   3. uv.lock records the exact version of every package, including dependencies of dependencies. Committing it means my laptops, CI and the serval all install the identical set
