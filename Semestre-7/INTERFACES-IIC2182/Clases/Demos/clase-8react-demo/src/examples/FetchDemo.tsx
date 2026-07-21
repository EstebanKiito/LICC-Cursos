import { useState, useEffect } from "react";

interface Post {
  id: number;
  title: string;
  body: string;
}

export function FetchDemo() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts?_limit=5")
      .then((res) => res.json())
      .then((data: Post[]) => {
        setPosts(data); // Overwrite, don't accumulate
        setLoading(false);
      });
  }, []); // Empty array = only on mount

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h2>Fetch with useEffect</h2>
      <p style={{ color: "#666", fontSize: 14 }}>
        Fetched {posts.length} posts from JSONPlaceholder on mount
      </p>
      <ul>
        {posts.map((post) => (
          <li key={post.id} style={{ marginBottom: 12 }}>
            <strong>{post.title}</strong>
            <p style={{ fontSize: 13, color: "#555" }}>{post.body.slice(0, 80)}...</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
