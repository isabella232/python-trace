# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore
from google.rpc import status_pb2 as gr_status  # type: ignore


__protobuf__ = proto.module(
    package="google.devtools.cloudtrace.v2",
    manifest={"Span", "AttributeValue", "StackTrace", "Module", "TruncatableString",},
)


class Span(proto.Message):
    r"""A span represents a single operation within a trace. Spans
    can be nested to form a trace tree. Often, a trace contains a
    root span that describes the end-to-end latency, and one or more
    subspans for its sub-operations. A trace can also contain
    multiple root spans, or none at all. Spans do not need to be
    contiguous&mdash;there may be gaps or overlaps between spans in
    a trace.

    Attributes:
        name (str):
            Required. The resource name of the span in the following
            format:

            ::

                projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]

            [TRACE_ID] is a unique identifier for a trace within a
            project; it is a 32-character hexadecimal encoding of a
            16-byte array.

            [SPAN_ID] is a unique identifier for a span within a trace;
            it is a 16-character hexadecimal encoding of an 8-byte
            array.
        span_id (str):
            Required. The [SPAN_ID] portion of the span's resource name.
        parent_span_id (str):
            The [SPAN_ID] of this span's parent span. If this is a root
            span, then this field must be empty.
        display_name (~.trace.TruncatableString):
            Required. A description of the span's
            operation (up to 128 bytes). Stackdriver Trace
            displays the description in the Google Cloud
            Platform Console.
            For example, the display name can be a qualified
            method name or a file name and a line number
            where the operation is called. A best practice
            is to use the same display name within an
            application and at the same call point. This
            makes it easier to correlate spans in different
            traces.
        start_time (~.timestamp.Timestamp):
            Required. The start time of the span. On the
            client side, this is the time kept by the local
            machine where the span execution starts. On the
            server side, this is the time when the server's
            application handler starts running.
        end_time (~.timestamp.Timestamp):
            Required. The end time of the span. On the
            client side, this is the time kept by the local
            machine where the span execution ends. On the
            server side, this is the time when the server
            application handler stops running.
        attributes (~.trace.Span.Attributes):
            A set of attributes on the span. You can have
            up to 32 attributes per span.
        stack_trace (~.trace.StackTrace):
            Stack trace captured at the start of the
            span.
        time_events (~.trace.Span.TimeEvents):
            A set of time events. You can have up to 32
            annotations and 128 message events per span.
        links (~.trace.Span.Links):
            Links associated with the span. You can have
            up to 128 links per Span.
        status (~.gr_status.Status):
            Optional. The final status for this span.
        same_process_as_parent_span (~.wrappers.BoolValue):
            Optional. Set this parameter to indicate
            whether this span is in the same process as its
            parent. If you do not set this parameter,
            Stackdriver Trace is unable to take advantage of
            this helpful information.
        child_span_count (~.wrappers.Int32Value):
            Optional. The number of child spans that were
            generated while this span was active. If set,
            allows implementation to detect missing child
            spans.
        span_kind (~.trace.Span.SpanKind):
            Optional. Distinguishes between spans generated in a
            particular context. For example, two spans with the same
            name may be distinguished using ``CLIENT`` (caller) and
            ``SERVER`` (callee) to identify an RPC call.
    """

    class SpanKind(proto.Enum):
        r"""Type of span. Can be used to specify additional relationships
        between spans in addition to a parent/child relationship.
        """
        SPAN_KIND_UNSPECIFIED = 0
        INTERNAL = 1
        SERVER = 2
        CLIENT = 3
        PRODUCER = 4
        CONSUMER = 5

    class Attributes(proto.Message):
        r"""A set of attributes, each in the format ``[KEY]:[VALUE]``.

        Attributes:
            attribute_map (Sequence[~.trace.Span.Attributes.AttributeMapEntry]):
                The set of attributes. Each attribute's key can be up to 128
                bytes long. The value can be a string up to 256 bytes, a
                signed 64-bit integer, or the Boolean values ``true`` and
                ``false``. For example:

                ::

                    "/instance_id": { "string_value": { "value": "my-instance" } }
                    "/http/request_bytes": { "int_value": 300 }
                    "abc.com/myattribute": { "bool_value": false }
            dropped_attributes_count (int):
                The number of attributes that were discarded.
                Attributes can be discarded because their keys
                are too long or because there are too many
                attributes. If this value is 0 then all
                attributes are valid.
        """

        attribute_map = proto.MapField(
            proto.STRING, proto.MESSAGE, number=1, message="AttributeValue",
        )

        dropped_attributes_count = proto.Field(proto.INT32, number=2)

    class TimeEvent(proto.Message):
        r"""A time-stamped annotation or message event in the Span.

        Attributes:
            time (~.timestamp.Timestamp):
                The timestamp indicating the time the event
                occurred.
            annotation (~.trace.Span.TimeEvent.Annotation):
                Text annotation with a set of attributes.
            message_event (~.trace.Span.TimeEvent.MessageEvent):
                An event describing a message sent/received
                between Spans.
        """

        class Annotation(proto.Message):
            r"""Text annotation with a set of attributes.

            Attributes:
                description (~.trace.TruncatableString):
                    A user-supplied message describing the event.
                    The maximum length for the description is 256
                    bytes.
                attributes (~.trace.Span.Attributes):
                    A set of attributes on the annotation. You
                    can have up to 4 attributes per Annotation.
            """

            description = proto.Field(
                proto.MESSAGE, number=1, message="TruncatableString",
            )

            attributes = proto.Field(
                proto.MESSAGE, number=2, message="Span.Attributes",
            )

        class MessageEvent(proto.Message):
            r"""An event describing a message sent/received between Spans.

            Attributes:
                type (~.trace.Span.TimeEvent.MessageEvent.Type):
                    Type of MessageEvent. Indicates whether the
                    message was sent or received.
                id (int):
                    An identifier for the MessageEvent's message
                    that can be used to match SENT and RECEIVED
                    MessageEvents. It is recommended to be unique
                    within a Span.
                uncompressed_size_bytes (int):
                    The number of uncompressed bytes sent or
                    received.
                compressed_size_bytes (int):
                    The number of compressed bytes sent or
                    received. If missing assumed to be the same size
                    as uncompressed.
            """

            class Type(proto.Enum):
                r"""Indicates whether the message was sent or received."""
                TYPE_UNSPECIFIED = 0
                SENT = 1
                RECEIVED = 2

            type = proto.Field(
                proto.ENUM, number=1, enum="Span.TimeEvent.MessageEvent.Type",
            )

            id = proto.Field(proto.INT64, number=2)

            uncompressed_size_bytes = proto.Field(proto.INT64, number=3)

            compressed_size_bytes = proto.Field(proto.INT64, number=4)

        time = proto.Field(proto.MESSAGE, number=1, message=timestamp.Timestamp,)

        annotation = proto.Field(
            proto.MESSAGE, number=2, oneof="value", message="Span.TimeEvent.Annotation",
        )

        message_event = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="value",
            message="Span.TimeEvent.MessageEvent",
        )

    class TimeEvents(proto.Message):
        r"""A collection of ``TimeEvent``\ s. A ``TimeEvent`` is a time-stamped
        annotation on the span, consisting of either user-supplied key:value
        pairs, or details of a message sent/received between Spans.

        Attributes:
            time_event (Sequence[~.trace.Span.TimeEvent]):
                A collection of ``TimeEvent``\ s.
            dropped_annotations_count (int):
                The number of dropped annotations in all the
                included time events. If the value is 0, then no
                annotations were dropped.
            dropped_message_events_count (int):
                The number of dropped message events in all
                the included time events. If the value is 0,
                then no message events were dropped.
        """

        time_event = proto.RepeatedField(
            proto.MESSAGE, number=1, message="Span.TimeEvent",
        )

        dropped_annotations_count = proto.Field(proto.INT32, number=2)

        dropped_message_events_count = proto.Field(proto.INT32, number=3)

    class Link(proto.Message):
        r"""A pointer from the current span to another span in the same
        trace or in a different trace. For example, this can be used in
        batching operations, where a single batch handler processes
        multiple requests from different traces or when the handler
        receives a request from a different project.

        Attributes:
            trace_id (str):
                The [TRACE_ID] for a trace within a project.
            span_id (str):
                The [SPAN_ID] for a span within a trace.
            type (~.trace.Span.Link.Type):
                The relationship of the current span relative
                to the linked span.
            attributes (~.trace.Span.Attributes):
                A set of attributes on the link. You have
                have up to  32 attributes per link.
        """

        class Type(proto.Enum):
            r"""The relationship of the current span relative to the linked
            span: child, parent, or unspecified.
            """
            TYPE_UNSPECIFIED = 0
            CHILD_LINKED_SPAN = 1
            PARENT_LINKED_SPAN = 2

        trace_id = proto.Field(proto.STRING, number=1)

        span_id = proto.Field(proto.STRING, number=2)

        type = proto.Field(proto.ENUM, number=3, enum="Span.Link.Type",)

        attributes = proto.Field(proto.MESSAGE, number=4, message="Span.Attributes",)

    class Links(proto.Message):
        r"""A collection of links, which are references from this span to
        a span in the same or different trace.

        Attributes:
            link (Sequence[~.trace.Span.Link]):
                A collection of links.
            dropped_links_count (int):
                The number of dropped links after the maximum
                size was enforced. If this value is 0, then no
                links were dropped.
        """

        link = proto.RepeatedField(proto.MESSAGE, number=1, message="Span.Link",)

        dropped_links_count = proto.Field(proto.INT32, number=2)

    name = proto.Field(proto.STRING, number=1)

    span_id = proto.Field(proto.STRING, number=2)

    parent_span_id = proto.Field(proto.STRING, number=3)

    display_name = proto.Field(proto.MESSAGE, number=4, message="TruncatableString",)

    start_time = proto.Field(proto.MESSAGE, number=5, message=timestamp.Timestamp,)

    end_time = proto.Field(proto.MESSAGE, number=6, message=timestamp.Timestamp,)

    attributes = proto.Field(proto.MESSAGE, number=7, message=Attributes,)

    stack_trace = proto.Field(proto.MESSAGE, number=8, message="StackTrace",)

    time_events = proto.Field(proto.MESSAGE, number=9, message=TimeEvents,)

    links = proto.Field(proto.MESSAGE, number=10, message=Links,)

    status = proto.Field(proto.MESSAGE, number=11, message=gr_status.Status,)

    same_process_as_parent_span = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.BoolValue,
    )

    child_span_count = proto.Field(
        proto.MESSAGE, number=13, message=wrappers.Int32Value,
    )

    span_kind = proto.Field(proto.ENUM, number=14, enum=SpanKind,)


class AttributeValue(proto.Message):
    r"""The allowed types for [VALUE] in a ``[KEY]:[VALUE]`` attribute.

    Attributes:
        string_value (~.trace.TruncatableString):
            A string up to 256 bytes long.
        int_value (int):
            A 64-bit signed integer.
        bool_value (bool):
            A Boolean value represented by ``true`` or ``false``.
    """

    string_value = proto.Field(
        proto.MESSAGE, number=1, oneof="value", message="TruncatableString",
    )

    int_value = proto.Field(proto.INT64, number=2, oneof="value")

    bool_value = proto.Field(proto.BOOL, number=3, oneof="value")


class StackTrace(proto.Message):
    r"""A call stack appearing in a trace.

    Attributes:
        stack_frames (~.trace.StackTrace.StackFrames):
            Stack frames in this stack trace. A maximum
            of 128 frames are allowed.
        stack_trace_hash_id (int):
            The hash ID is used to conserve network bandwidth for
            duplicate stack traces within a single trace.

            Often multiple spans will have identical stack traces. The
            first occurrence of a stack trace should contain both the
            ``stackFrame`` content and a value in ``stackTraceHashId``.

            Subsequent spans within the same request can refer to that
            stack trace by only setting ``stackTraceHashId``.
    """

    class StackFrame(proto.Message):
        r"""Represents a single stack frame in a stack trace.

        Attributes:
            function_name (~.trace.TruncatableString):
                The fully-qualified name that uniquely
                identifies the function or method that is active
                in this frame (up to 1024 bytes).
            original_function_name (~.trace.TruncatableString):
                An un-mangled function name, if ``function_name`` is
                `mangled <http://www.avabodh.com/cxxin/namemangling.html>`__.
                The name can be fully-qualified (up to 1024 bytes).
            file_name (~.trace.TruncatableString):
                The name of the source file where the
                function call appears (up to 256 bytes).
            line_number (int):
                The line number in ``file_name`` where the function call
                appears.
            column_number (int):
                The column number where the function call
                appears, if available. This is important in
                JavaScript because of its anonymous functions.
            load_module (~.trace.Module):
                The binary module from where the code was
                loaded.
            source_version (~.trace.TruncatableString):
                The version of the deployed source code (up
                to 128 bytes).
        """

        function_name = proto.Field(
            proto.MESSAGE, number=1, message="TruncatableString",
        )

        original_function_name = proto.Field(
            proto.MESSAGE, number=2, message="TruncatableString",
        )

        file_name = proto.Field(proto.MESSAGE, number=3, message="TruncatableString",)

        line_number = proto.Field(proto.INT64, number=4)

        column_number = proto.Field(proto.INT64, number=5)

        load_module = proto.Field(proto.MESSAGE, number=6, message="Module",)

        source_version = proto.Field(
            proto.MESSAGE, number=7, message="TruncatableString",
        )

    class StackFrames(proto.Message):
        r"""A collection of stack frames, which can be truncated.

        Attributes:
            frame (Sequence[~.trace.StackTrace.StackFrame]):
                Stack frames in this call stack.
            dropped_frames_count (int):
                The number of stack frames that were dropped
                because there were too many stack frames.
                If this value is 0, then no stack frames were
                dropped.
        """

        frame = proto.RepeatedField(
            proto.MESSAGE, number=1, message="StackTrace.StackFrame",
        )

        dropped_frames_count = proto.Field(proto.INT32, number=2)

    stack_frames = proto.Field(proto.MESSAGE, number=1, message=StackFrames,)

    stack_trace_hash_id = proto.Field(proto.INT64, number=2)


class Module(proto.Message):
    r"""Binary module.

    Attributes:
        module (~.trace.TruncatableString):
            For example: main binary, kernel modules, and
            dynamic libraries such as libc.so, sharedlib.so
            (up to 256 bytes).
        build_id (~.trace.TruncatableString):
            A unique identifier for the module, usually a
            hash of its contents (up to 128 bytes).
    """

    module = proto.Field(proto.MESSAGE, number=1, message="TruncatableString",)

    build_id = proto.Field(proto.MESSAGE, number=2, message="TruncatableString",)


class TruncatableString(proto.Message):
    r"""Represents a string that might be shortened to a specified
    length.

    Attributes:
        value (str):
            The shortened string. For example, if the original string is
            500 bytes long and the limit of the string is 128 bytes,
            then ``value`` contains the first 128 bytes of the 500-byte
            string.

            Truncation always happens on a UTF8 character boundary. If
            there are multi-byte characters in the string, then the
            length of the shortened string might be less than the size
            limit.
        truncated_byte_count (int):
            The number of bytes removed from the original
            string. If this value is 0, then the string was
            not shortened.
    """

    value = proto.Field(proto.STRING, number=1)

    truncated_byte_count = proto.Field(proto.INT32, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
