using System.Collections.Generic;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;
using RosMessageTypes.Std;
using RosMessageTypes.Actionlib;

namespace RosMessageTypes.Moveit
{
    public class PlaceActionFeedback : ActionFeedback<PlaceFeedback>
    {
        public const string RosMessageName = "moveit_msgs/PlaceActionFeedback";

        public PlaceActionFeedback() : base()
        {
            this.feedback = new PlaceFeedback();
        }

        public PlaceActionFeedback(Header header, GoalStatus status, PlaceFeedback feedback) : base(header, status)
        {
            this.feedback = feedback;
        }
        public override List<byte[]> SerializationStatements()
        {
            var listOfSerializations = new List<byte[]>();
            listOfSerializations.AddRange(this.header.SerializationStatements());
            listOfSerializations.AddRange(this.status.SerializationStatements());
            listOfSerializations.AddRange(this.feedback.SerializationStatements());

            return listOfSerializations;
        }

        public override int Deserialize(byte[] data, int offset)
        {
            offset = this.header.Deserialize(data, offset);
            offset = this.status.Deserialize(data, offset);
            offset = this.feedback.Deserialize(data, offset);

            return offset;
        }

    }
}
