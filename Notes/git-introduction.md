# Git Technical Overview

## Core Architecture

**Distributed Version Control System (DVCS)**
- Every clone is a complete repository with full history
- No single point of failure
- Works offline
- Peer-to-peer architecture

## Data Model

**Object Store**
- **Blob**: File content (immutable)
- **Tree**: Directory structure, references blobs/trees
- **Commit**: Snapshot with metadata (author, timestamp, message)
- **Tag**: Named reference to specific commit

**Content-Addressable Storage**
- Objects identified by SHA-1 hash of content
- Ensures data integrity
- Enables deduplication

## Repository Structure


.git/
├── objects/        # Object database (blobs, trees, commits)
├── refs/          # Branch and tag references
├── HEAD           # Current branch pointer
├── index          # Staging area
├── config         # Repository configuration
└── hooks/         # Custom scripts


## Key Concepts

**Three States**
1. **Working Directory**: Current files
2. **Staging Area (Index)**: Prepared changes
3. **Repository**: Committed history

**References**
- **HEAD**: Current commit/branch
- **Branches**: Movable pointers to commits
- **Tags**: Fixed pointers to commits
- **Remote refs**: Track remote repository state

## Core Operations

**Local Operations**
- `add`: Stage changes to index
- `commit`: Create snapshot from staged changes
- `checkout`: Switch branches/restore files
- `merge`: Combine branch histories
- `rebase`: Replay commits on different base

**Remote Operations**
- `clone`: Copy remote repository
- `fetch`: Download remote changes
- `pull`: Fetch + merge
- `push`: Upload local changes

## Most Common Git Commands

### Repository Setup
bash
git init                    # Initialize new repository
git clone <url>            # Clone remote repository
git config --global user.name "Name"     # Set username
git config --global user.email "email"   # Set email


### Basic Workflow
bash
git status                 # Show working tree status
git add <file>            # Stage specific file
git add .                 # Stage all changes
git add -A                # Stage all changes including deletions
git commit -m "message"   # Commit staged changes
git commit -am "message"  # Stage and commit all tracked files


### Viewing History
bash
git log                   # Show commit history
git log --oneline        # Compact commit history
git log --graph          # Show branch graph
git show <commit>        # Show specific commit details
git diff                 # Show unstaged changes
git diff --staged        # Show staged changes
git diff <commit1> <commit2>  # Compare commits


### Branching
bash
git branch               # List local branches
git branch <name>        # Create new branch
git branch -d <name>     # Delete branch
git checkout <branch>    # Switch to branch
git checkout -b <name>   # Create and switch to branch
git switch <branch>      # Modern way to switch branches
git switch -c <name>     # Create and switch (modern)
git merge <branch>       # Merge branch into current


### Remote Operations
bash
git remote -v            # Show remote repositories
git remote add origin <url>  # Add remote repository
git fetch                # Download remote changes
git pull                 # Fetch and merge from remote
git push                 # Upload changes to remote
git push -u origin <branch>  # Push and set upstream
git push --force         # Force push (dangerous)


### Undoing Changes
bash
git checkout -- <file>   # Discard working directory changes
git restore <file>       # Modern way to discard changes
git restore --staged <file>  # Unstage file
git reset HEAD <file>    # Unstage file (older method)
git reset --soft HEAD~1  # Undo last commit, keep changes staged
git reset --hard HEAD~1  # Undo last commit, discard changes
git revert <commit>      # Create new commit that undoes changes


### Stashing
bash
git stash                # Temporarily save changes
git stash pop            # Apply and remove latest stash
git stash list           # Show all stashes
git stash apply          # Apply stash without removing
git stash drop           # Delete specific stash


### Tagging
bash
git tag                  # List tags
git tag <name>           # Create lightweight tag
git tag -a <name> -m "message"  # Create annotated tag
git push --tags          # Push tags to remote


### Advanced Operations
bash
git rebase <branch>      # Replay commits on different base
git rebase -i HEAD~3     # Interactive rebase last 3 commits
git cherry-pick <commit> # Apply specific commit to current branch
git blame <file>         # Show who changed each line
git bisect start         # Start binary search for bug
git clean -fd            # Remove untracked files and directories


## Branching Model

**Lightweight Branches**
- Just pointers to commits (~40 bytes)
- Fast creation/switching
- Enables feature branches, experimentation

**Merge Strategies**
- **Fast-forward**: Linear history
- **Three-way merge**: Creates merge commit
- **Squash**: Combine multiple commits

## Advanced Features

**Hooks**
- Pre/post commit, push, receive
- Custom validation, automation
- Client-side and server-side

**Submodules**
- Embed repositories within repositories
- Track specific commits of dependencies

**Worktrees**
- Multiple working directories per repository
- Parallel development on different branches

## Performance Characteristics

**Optimizations**
- Delta compression for similar objects
- Pack files for efficient storage/transfer
- Shallow clones for large repositories
- Partial clone for monorepos

**Scalability**
- Handles repositories with millions of files
- Efficient for binary files with LFS extension
- Distributed nature scales horizontally

## Security Model

**Cryptographic Integrity**
- SHA-1 hashing (transitioning to SHA-256)
- Tamper detection
- Signed commits/tags with GPG

**Access Control**
- Repository-level permissions
- Branch protection rules
- Audit trails

## Common Workflows

### Feature Branch Workflow
bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Create pull request
git checkout main
git pull
git branch -d feature/new-feature


### Hotfix Workflow
bash
git checkout main
git pull
git checkout -b hotfix/critical-bug
# Fix bug
git add .
git commit -m "Fix critical bug"
git push -u origin hotfix/critical-bug
# Merge to main and develop


Git's design prioritizes data integrity, performance, and distributed collaboration while maintaining simplicity in its core concepts.
