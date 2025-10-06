import React from "react";

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, err: null };
  }
  static getDerivedStateFromError(err) {
    return { hasError: true, err };
  }
  componentDidCatch(err, info) {
    console.error("ErrorBoundary catch:", err, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div className="m-4 p-4 rounded-xl bg-red-500/20 border border-red-500/40">
          <div className="font-semibold mb-1">レンダリング中にエラーが発生しました</div>
          <pre className="text-xs whitespace-pre-wrap opacity-80">{String(this.state.err)}</pre>
        </div>
      );
    }
    return this.props.children;
  }
}
