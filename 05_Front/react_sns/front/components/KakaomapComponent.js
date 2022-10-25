import React, { forwardRef } from "react";


const KakaomapComponent = forwardRef((props, ref) => {
    return (React.createElement("div", { style: { width: "400px", height: "300px" } },
        React.createElement("div", { ref: ref, style: { width: "100%", height: "100%" } })));
});
export default KakaomapComponent;
