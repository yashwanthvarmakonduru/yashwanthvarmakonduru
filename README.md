# Yashwanth Varma

I'm Yashwanth, a full stack engineer based in Hyderabad who builds software end to end and cares about getting the hard parts right.

My recent work is four production style projects, each aimed at a problem that is easy to get wrong. In Synapse, a local first collaborative workspace, I used a CRDT so that two people can edit the same paragraph offline and merge without losing anything, and I checked the guarantee with a property based test that ran 10,000 times. In Atlas AI, a document copilot, I built hybrid retrieval with a tenant filter so every answer cites its source page, and I measured it: 95.4% recall@10 on an evaluation set and zero cross tenant leaks in the isolation tests.

In Deccan Estates, a Hyderabad property platform, I split the verification logic into a Go service and kept it in step with the TypeScript original through 1,200 shared test cases. In Meridian, I published an accessible React component library to npm, with accessibility and visual regression checks that block a merge when they fail.

What drives me is the gap between software that works in a demo and software that holds up in use. I write down my design decisions, measure my own claims, and publish what I get wrong. I'm looking for my first full stack or frontend engineering role, where I can keep building systems that stay reliable at scale.

*"The computer programmer is a creator of universes for which he alone is the lawgiver."* ~ Weizenbaum

[![Email](https://img.shields.io/badge/Email-yashwanthvarma74%40gmail.com-1f6feb?style=flat-square&logo=gmail&logoColor=white)](mailto:yashwanthvarma74@gmail.com)
[![npm](https://img.shields.io/badge/npm-%40yashwanthvarma74%2Freact-cb3837?style=flat-square&logo=npm&logoColor=white)](https://www.npmjs.com/package/@yashwanthvarma74/react)

## Selected work

| Project | What it does | Links |
| --- | --- | --- |
| **Atlas AI** | Private knowledge copilot. Every answer cites its source page. Hybrid retrieval with a tenant filter, 95.4% recall@10 on its evaluation set. | [Demo](https://atlas-ai-seven-vert.vercel.app) / [Code](https://github.com/yashwanthvarmakonduru/Atlas-AI) |
| **Synapse** | Local first collaborative workspace. Documents and a shared canvas that work offline and merge on reconnect, using Yjs and Redis fan out. | [Demo](https://synapse-app-beta.vercel.app) / [Code](https://github.com/yashwanthvarmakonduru/synapse) |
| **Deccan Estates** | Hyderabad real estate platform with search, a verification report service in Go, owner posting and an inventory search assistant. | [Demo](https://deccan-estates-zeta.vercel.app) / [Code](https://github.com/yashwanthvarmakonduru/deccan-estates) |
| **Meridian** | Accessible React component library on npm. Design tokens, three themes, Storybook, accessibility and visual regression checks in CI. | [Storybook](https://yashwanthvarmakonduru.github.io/designSystem/) / [Code](https://github.com/yashwanthvarmakonduru/designSystem) |

## Stack

TypeScript, React, Next.js, Node.js, Go, PostgreSQL, MongoDB, Redis, Docker, GitHub Actions

## Writing

[Why I used a CRDT and not OT for a collaborative editor](https://dev.to/yashwanthvarma/why-i-used-a-crdt-and-not-ot-for-a-collaborative-editor-54d5) on dev.to

## Snake

A snake that eats my contribution graph. It is regenerated every 12 hours by a GitHub Action.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yashwanthvarmakonduru/yashwanthvarmakonduru/output/github-snake-dark.svg">
  <img alt="Snake eating my contribution graph" src="https://raw.githubusercontent.com/yashwanthvarmakonduru/yashwanthvarmakonduru/output/github-snake.svg">
</picture>
